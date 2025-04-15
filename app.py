import streamlit as st
from utils.solver import calculate_net_balances, simplify_debts
from utils.visualizer import create_graph, draw_graph

def main():
    st.set_page_config(layout="wide")
    st.title("Debt Simplification Visualizer")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Input Transactions")
        num_people = st.slider("Number of people", 2, 20, 5)
        nodes = [f"Person {i+1}" for i in range(num_people)]
        
        if "transactions" not in st.session_state:
            st.session_state.transactions = []

        with st.form("transaction_form"):
            cols = st.columns(3)
            with cols[0]:
                from_person = st.selectbox("From", nodes)
            with cols[1]:
                to_person = st.selectbox("To", nodes)
            with cols[2]:
                amount = st.number_input("Amount ($)", min_value=1)

            submitted = st.form_submit_button("Add Transaction")
            if submitted:
                if from_person == to_person:
                    st.warning("Sender and receiver must be different.")
                else:
                    st.session_state.transactions.append((
                        nodes.index(from_person),
                        nodes.index(to_person),
                        amount
                    ))
        
        st.write("Current Transactions:")
        for t in st.session_state.transactions:
            st.write(f"{nodes[t[0]]} → {nodes[t[1]]}: ${t[2]}")

        if st.button("Clear Transactions"):
            st.session_state.transactions = []
    
    with col2:
        if st.session_state.transactions:
            st.header("Results")
            net_balances = calculate_net_balances(nodes, st.session_state.transactions)
            simplified = simplify_debts(nodes, net_balances)
            
            st.subheader("Original Transactions")
            G_original = create_graph(nodes, st.session_state.transactions)
            original_img = draw_graph(G_original, "Original Debt Network")
            st.image(original_img)
            
            st.subheader("Simplified Transactions")
            G_simplified = create_graph(nodes, simplified)
            simplified_img = draw_graph(G_simplified, "Simplified Debt Settlement")
            st.image(simplified_img)

if __name__ == "__main__":
    main()
