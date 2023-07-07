/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head){
  struct ListNode* cur = head;
  struct ListNode* pre = head;
  int pre_val = -200;

  while (cur != NULL) {
    //have duplicate
    if (cur->next != NULL && cur->val == cur->next->val) {
        int target_val = cur->val;
        //find the lats duplicate
        while (cur!= NULL && cur->val == target_val) {
            cur = cur->next;
        }
        //the duplicate is head 
        if (target_val == head->val)
            head = cur;
        //the duplicate not head 
        else 
            pre->next = cur;
    } 
    //not have duplicate
    else {
      pre = cur;
      cur = cur->next;
    }
  }
  return head;
}