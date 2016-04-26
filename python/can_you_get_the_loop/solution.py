def loop_size(node):
    count = 1
    node_s1 = node.next; node_s2 = node.next.next
    while node_s1 != node_s2:
        count += 1
        node_s1 = node_s1.next
        node_s2 = node_s2.next.next
    cur_node = node_s1
    count_circel = 1
    cur_node = cur_node.next
    while cur_node != node_s1:
        cur_node = cur_node.next
        count_circel += 1
    return count_circel