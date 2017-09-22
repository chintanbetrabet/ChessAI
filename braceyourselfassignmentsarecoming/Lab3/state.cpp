#include<bits/stdc++.h>
#include <tuple> 

using namespace std;

class state
{
    int rows, cols;
    vector<string> board;

    public :
	
		/* basic methods for constructing and proper hashing of State objects */
        state(int n_rows, int n_col)
        {
            this->rows = n_rows;
            this->cols = n_col;
            board.resize(n_rows,string(n_col,'.'));
        }

        bool equals(state other)
        {
            if(this->board.size() != other.board.size())
                return false;

            for(int i=0;i<this->board.size();i++)
                if(this->board[i]!=other.board[i])
                    return false;
            return true;
        }

        state clone()
        {
            state new_state(this->rows,this->cols);
            for(int i=0;i<this->rows;i++)
                new_state.board[i]=this->board[i];
            return new_state;
        }
		
		
		/* returns a list of actions that can be taken from the current state
		actions are integers representing the column where a coin can be dropped */
        vector<int> getLegalActions()
        {
            vector<int> actions;
			for(int j=0; j<this->cols; j++)
				if(this->board[0][j]=='.')
					actions.push_back(j);
			return actions;
        }
		
		
		/* returns a State object that is obtained by the agent (parameter)
		performing an action (parameter) on the current state */
        state generateSuccessor(char agent, int action)
		{
			int row;
			for(row=0; row<this->rows && this->board[row][action]!='X' && this->board[row][action]!='O'; row++);
			state new_state=this->clone();
			new_state.board[row-1][action]=agent;

			return new_state;
		}

		/* Print's the current state's board in a nice pretty way */
		void printBoard()
		{
			cout<<string(2*this->cols, '-')<<endl;
		    for(int i=0;i<this->board.size();i++){
				for(int j=0; j<this->cols; j++)
		        	cout<<this->board[i][j]<<" ";
				cout<<endl;
			}
			cout<<string(2*this->cols, '-')<<endl;
		}

		/* returns True/False if the agent(parameter) has won the game
		by checking all rows/columns/diagonals for a sequence of >=4 */
		bool isGoal(char agent)
		{
	
			string win=string(4, agent);

			//check rows
			for(int i=0; i<this->rows; i++)
				if(this->board[i].find(win)!=string::npos)
					return true;
		
			//check cols
			for(int j=0; j<this->cols; j++){
				string col="";
				for(int i=0; i<this->rows; i++)
					col+=this->board[i][j];
				
				if(col.find(win)!=string::npos)
					return true;
			}
		
			//check diags
			vector<tuple<int,int>> pos_right;
			vector<tuple<int,int>> pos_left;
		
			for(int j=0; j<this->cols-4+1; j++)
				pos_right.push_back(tuple<int,int>(0,j));
			for(int j=4-1; j<this->cols; j++)
				pos_left.push_back(tuple<int,int>(0,j));
			for(int i=1; i<this->rows-4+1; i++){
				pos_right.push_back(tuple<int,int>(i,0));
				pos_left.push_back(tuple<int,int>(i,this->cols-1));
			}
	
			//check right diags
			for (tuple<int,int> p : pos_right) {
				string d="";
				int x=get<0>(p), y=get<1>(p);
				while(true){				
					if (x>=this->rows||y>=this->cols)
						break;
					d+=this->board[x][y];
					x+=1; y+=1;
				}
				if(d.find(win)!=string::npos)
					return true;
			}
		
			//check left diags
			for (tuple<int,int> p: pos_left) {
				string d="";
				int x=get<0>(p), y=get<1>(p);
				while(true){
					if(y<0||x>=this->rows||y>=this->cols)
						break;
					d+=this->board[x][y];
					x+=1; y-=1;
				}
				if(d.find(win)!=string::npos)
					return true;
			}
		
			return false;
	}

		/* returns the value of each state for minimax to min/max over at
		zero depth. Right now it's pretty trivial, looking for only goal states.
		(This would be perfect for infinite depth minimax. Not so great for d=2) */
		double evaluationFunction()
		{
			if (this->isGoal('O'))
				return 1000.0;
			else if (this->isGoal('X'))
				return -1000.0;

			return 0.0;
		}

};


int main(void)
{
    state s(6,7);
	s.printBoard();

}
