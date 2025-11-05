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
    ListNode* findNthNode(ListNode* temp,int k){
        int cnt=1;
        while(temp!=NULL){
            if(cnt==k)return temp;
            cnt++;
            temp=temp->next;
        }
        return temp;
    }
    ListNode* rotateRight(ListNode* head, int k) {
        if(head==NULL|| k==0)return head;
        ListNode* temp=head;
        int count=1;
        while(temp->next!=NULL){
            count++;
            temp=temp->next;
        }
        if(k%count == 0)return head;
        k=k%count;
        temp->next=head;
        ListNode* newLastNode=findNthNode(head,count-k);
        head=newLastNode->next;
        newLastNode->next=NULL;
        return head;

    }
};