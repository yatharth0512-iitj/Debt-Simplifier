from .binary_heap import BinaryHeap

def calculate_net_balances(nodes, edges):
    """Calculate net balances for each person"""
    sz = len(nodes)
    vals = [0] * sz
    for from_, to, amount in edges:
        vals[to] += amount
        vals[from_] -= amount
    return vals

def simplify_debts(nodes, net_balances):
    """Simplify debts using heap approach"""
    pos_heap = BinaryHeap()
    neg_heap = BinaryHeap()
    
    for i, balance in enumerate(net_balances):
        if balance > 0:
            pos_heap.insert((balance, i))
        elif balance < 0:
            neg_heap.insert((-balance, i))
    
    new_edges = []
    
    while not pos_heap.empty() and not neg_heap.empty():
        max_pos = pos_heap.extractMax()
        max_neg = neg_heap.extractMax()
        
        amt = min(max_pos[0], max_neg[0])
        to = max_pos[1]
        from_ = max_neg[1]
        
        new_edges.append((from_, to, amt))
        
        if max_pos[0] > amt:
            pos_heap.insert((max_pos[0] - amt, to))
        if max_neg[0] > amt:
            neg_heap.insert((max_neg[0] - amt, from_))
    
    return new_edges