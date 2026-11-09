class Solution {
public:
    bool isPalindrome(string s) {
        
        vector<char> backwards;
        vector<char> myword;

        // meter char by char en my word
        for (char c : s ){
            if (isalnum(c)) {
                myword.push_back(std::tolower(c));
            }

        }

        // // see char by char
        // for (int i = 0 ; i < myword.size(); i++){
        //     cout << myword[i]<< "  " ;
        // }

        // // use iterators for the code
        // for (auto it = myword.begin(); it != myword.end(); ++it) {
        //     cout << *it << endl;

        // }

        // reading backwards
        for (auto it = myword.end(); it != myword.begin(); ) {
            --it;
            //cout << *it << endl;

            backwards.push_back(*it);
        }

        // si no tienen el msm size, es false
        if ( myword.size() != backwards.size()){
            return false;
        }


        int count = 0;
        for (int i = 0; i < myword.size(); i++){
            if (myword[i] != backwards[i]){
                return false;

            }


        }

        // if (count == myword.size()){
        //     return true;
        // }

        return true;
        
    
    }
};
