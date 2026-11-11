class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        for( int  i = 0; i < matrix.size(); i++ ){
            
            for (int  y = 0; y < matrix[i].size(); y++){
                if ( matrix[i][y] == target){
                    return true ;

                }

            }


        }
        return false;
    }   
};
