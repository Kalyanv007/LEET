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
    int pairSum(ListNode* head) {
        ListNode* fast=head;
        ListNode* slow=head;
        while(fast!=NULL && fast->next!=NULL){
            fast=fast->next->next;
            slow=slow->next;
        }

        ListNode* secondhalf=reverseList(slow);
        ListNode* firsthalf=head;
        int maxSum=0;
        while(secondhalf!=NULL){
            maxSum=max(maxSum,firsthalf->val + secondhalf->val);
            firsthalf=firsthalf->next;
            secondhalf=secondhalf->next;
        }
        return maxSum;
    }
    ListNode* reverseList(ListNode* head) {
        ListNode* temp=head;
        ListNode* prev=NULL;
        while(temp!=NULL){
            ListNode* front=temp->next;
            temp->next=prev;
            prev=temp;
            temp=front;

        }
        return prev;
    }
};