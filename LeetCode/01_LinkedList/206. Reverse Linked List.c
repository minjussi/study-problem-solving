/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
// head: memory address that points first node
// node size: int val (4 byte)+ ListNode *next (8 byte)
struct ListNode* reverseList(struct ListNode* head) {
    // prev: start with NULL , previous node address
    // curr: start with head, current node address
    // next_curr: store next node temporarily
    struct ListNode* prev = NULL;
    struct ListNode* curr = head;
    struct ListNode* next_curr = NULL;

    // if curr is NULL -> there's no more node
    while (curr != NULL) {
        next_curr = curr->next;
        // current node points previous node (change direction)
        curr->next = prev;
        prev = curr;
        curr = next_curr;
    }
    
    // after while loop prev becomes new head
    // leet code runs main code automatically
    return prev;
}
