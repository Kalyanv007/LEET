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
    ListNode* removeElements(ListNode* head, int val) {
        while(head!=NULL && head->val==val){
            ListNode* temp=head;
            head=head->next;
            delete(temp);
        }
        ListNode* temp=head;
        ListNode* prev=NULL;
        while(temp!=NULL && temp->next!=NULL){
            if(temp->next->val==val){
                ListNode* cur=temp->next;
                temp->next=temp->next->next;
                delete(cur);
            }
            else{
                temp=temp->next;
            }
        }
        return head;
    }
};