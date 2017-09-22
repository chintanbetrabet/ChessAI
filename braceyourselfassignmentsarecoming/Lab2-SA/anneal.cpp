#include<bits/stdc++.h>
#include<chrono>
#include<random>
#include <stdlib.h>

using namespace std;
#define ull unsigned long long

unsigned seed = chrono::system_clock::now().time_since_epoch().count();
default_random_engine gen(seed);

unordered_map<int,vector<int>> g;
unsigned long long N,E,v1,v2,colours;
string gid;
vector<int> parse(string state){

	stringstream lineStream(state);
    vector<int> numbers;
	int num;
	while (lineStream >> num)
		numbers.push_back(num);
	return numbers;
}



void init(string &current,unsigned long long colours)
{
    uniform_int_distribution<int> distr(48,47+colours);
    for(unsigned i=0; i<current.length();i++)
        current[i]=distr(gen);
}



void display_G(string state, double timeout, int save){
	
	
	
	ostringstream sstream;
	for(int i=0; i<state.length(); i++){
		sstream<<(int(state.at(i))-'0')<<" ";
	}	
	
	ostringstream cmd;
	cmd<<"python show_graph.py "<<gid<<" \""<<sstream.str()<<"\" "<<timeout<<" "<<save;
	
	char command[100];
	sprintf (command, cmd.str().c_str());  
	system(command);
	
	/*uncomment the next line if you want to pause every visualization
	until you hit ENTER, to get a better look at the pretty graph*/
	//cin.get();
	
	

}
/*-----------------------------YOU NEED TO EDIT THESE FUNCTIONS----------------------------------*/

/*Find a good objective function to MINIMIZE.
Remember, your ideal, best, amazing solution needs to have the
lowest function value*/
unsigned long long cost_fn(string state)
{
	//FILL IN YOUR CODE HERE- and return the value of the state
	return cost;

}


/*Try out all the temperature functions you can think of- Slow, fast, sinusoidal.
No, not sinusoidal.*/
double schedule (double t)
{
	//FILL IN YOUR CODE HERE- and return the new temperature value
    return new_t;
}


/* Remember, ANY local move works. Even extremely trivial ones.
We're hoping you'll come up with a decently complex local move --
with a good balance of computational expensiveness and utility.
The more complex local moves will help the solution converge faster,
and that's what you should be aiming to do */
string move(string current)
{
	//FILL IN YOUR CODE HERE- and return the new state
    return next;
}

/*------------------------------------------------------------------------------------------*/


int main(int argc, char**argv)
{


	/* disp(the value 300 here) controls after how many iterations you want to see your graph
	set it to a negative number if you don't want to see it at all.
	(you'll still see your final graph)*/
	/*--------------YOU NEED TO EDIT THESE VALUES-------------*/
	int disp=300;
	double t= 0.0; //initial temperature
	/*-------------------------------------------------------*/
	
	
	ifstream fin;
    fin.open(argv[1]);
	
	int idx=string(argv[1]).find("gc_");
	gid=string(argv[1]).substr(idx+3);
	
    colours = atoll(argv[2]);
    fin>>N>>E;

    for(int i=0;i<E;i++)
    {
        fin>>v1>>v2;
        g[v1].push_back(v2);
		g[v2].push_back(v1);
    }
    
    string current(N,0);

    init(current,colours);
    string best_cost(current);
	
	int iters=-1;
    while(t>1)
    {   unsigned long long cst_fn = cost_fn(current);
        ull bst_cst = cost_fn(best_cost);
        t= schedule(t);
        string next = move(current);
		
        cout<<"BEST: "<<bst_cst<<"    T:"<<t<<"    C:"<<cst_fn<<endl;
		
		if(disp>0 && iters%disp==0)
			display_G(next, 0.5, 0);
		iters+=1;
		
		ull  nxt_cst= cost_fn(next);
        long long  del_e =nxt_cst-cst_fn;
        if(del_e <0)
        {
            current = next;
			
			if(nxt_cst<bst_cst){
				bst_cst = nxt_cst;
				best_cost=next;
			}
				
        }
        else
        {
            uniform_real_distribution<double> distr(0.0,1.0);
           long double val1 = distr(gen);
            long double val2 = (long double)1.0/exp(((long double)del_e)/(long double)t);

            if(val1<= val2)
                current=next;
        }

    }
	
	ostringstream sstream;
	for(int i=0; i<best_cost.length(); i++){
		sstream<<(int(best_cost.at(i))-'0')<<" ";
	}	
	
    cout<<current<<" "<<cost_fn(current)<<endl;
    cout<<"Best :" << sstream.str()<<" with cost:"<<cost_fn(best_cost)<<"\n\n\n\n";
	
	display_G(best_cost, 100, 1);
	
}
