/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode* fast=head;
        ListNode* slow=head;
        ListNode* first=head;
        for(int i=0;i<k-1;i++){
            first=first->next;
            fast=fast->next;
        }
        while(fast->next!=NULL){
            fast=fast->next;
            slow=slow->next;
        }
        int temp=first->val;
        first->val=slow->val;
        slow->val=temp;
        return head;
    }
};