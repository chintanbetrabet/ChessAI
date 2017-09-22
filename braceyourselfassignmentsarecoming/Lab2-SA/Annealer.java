import java.util.*;
import java.io.*;


class Annealer
{

	int[] init_state;
	int[] best_state;
	double best_cost;
	int disp;
	String gid;
	
	int N, E, colors;
	HashMap<Integer,ArrayList<Integer>> G = new HashMap<Integer,ArrayList<Integer>>();
	
	void parse(String filename) throws FileNotFoundException {
	
		Scanner s=new Scanner(new File(filename));
		this.N=s.nextInt(); this.E=s.nextInt();
		for(int i=0; i<this.E; i++){
			int u=s.nextInt(), v=s.nextInt();
			
			if(!this.G.containsKey(u)){
				ArrayList<Integer> nbhs= new ArrayList<Integer>();
				nbhs.add(v);
				this.G.put(u,nbhs);
			}
			else{
				ArrayList<Integer> nbhs=this.G.get(u);
				nbhs.add(v);
				this.G.put(u,nbhs);
			}
			
			if(!this.G.containsKey(v)){
				ArrayList<Integer> nbhs= new ArrayList<Integer>();
				nbhs.add(u);
				this.G.put(v,nbhs);
			}
			else{
				ArrayList<Integer> nbhs=this.G.get(v);
				nbhs.add(u);
				this.G.put(v,nbhs);
			}
			
			
		}
		
		s.close();
	}
	
	
	Annealer(int colors, int disp, String filename) throws FileNotFoundException{
		
		parse(filename);
		this.init_state=new int[this.N];
		this.best_state=init_state.clone();
		this.best_cost=cost_fn(this.best_state);
		this.colors=colors;
		this.disp=disp;
		
		int idx=filename.indexOf("gc_");
		this.gid=filename.substring(idx+3);
		
	}

	void display_G(int[] state, double timeout, int save){
		
		String statestr="";
		for(int i=0; i<state.length; i++)
			statestr+=state[i]+" ";
			
		ProcessBuilder pb = new ProcessBuilder("python","show_graph.py", gid, statestr, ""+timeout, ""+save);
		
		try {Process p = pb.start();}
		catch (IOException ioe){System.out.println("IO-fail");}
		try {Thread.sleep(1000);}
		catch (InterruptedException ioe){System.out.println("Interrupt-fail");}
	}


	double accept(double delta, double temp){
		if(delta<0)
			return 1.0;
		return Math.exp(-delta/temp);
	}
	
	void anneal(double temp)
	{	
		int[] current_state=this.best_state;
		double current_cost=this.best_cost;

		int iters=-1;
		while(temp > 1){
			
			System.out.format("BEST: %f  T: %f   C: %f \n",this.best_cost, temp, current_cost);
			if(this.disp>0 && iters%this.disp==0)
				this.display_G(current_state, 0.5, 0);
			iters+=1;

			int[] state=local_move(current_state);
			double delta=cost_fn(state)-cost_fn(current_state);
			
			if (accept(delta, temp) > Math.random()){
				current_state=state;
				current_cost+=delta;
				
				if(current_cost<this.best_cost){
					this.best_cost=current_cost;
					this.best_state=state.clone();
				}
			}			
			temp=cool_func(temp);
		}
	}
		
	/*-----------------------------YOU NEED TO EDIT THESE FUNCTIONS----------------------------------*/	
	
	/* Remember, ANY local move works. Even extremely trivial ones.
	We're hoping you'll come up with a decently complex local move --
	with a good balance of computational expensiveness and utility.
	The more complex local moves will help the solution converge faster,
	and that's what you should be aiming to do */
	int[] local_move(int[] state){
		//FILL IN YOUR CODE HERE- and return the new state
		return new_state;
	}
	
	/*Try out all the temperature functions you can think of- Slow, fast, sinusoidal.
	No, not sinusoidal.*/
	double cool_func(double temp){
		//FILL IN YOUR CODE HERE- and return the new temperature value
		return new_temp;
	}
	
	/*Find a good objective function to MINIMIZE.
	Remember, your ideal, best, amazing solution needs to have the
	lowest function value*/
	double cost_fn(int[] state){
		//FILL IN YOUR CODE HERE- and return the value of the state
		return cost;
	}

	/*------------------------------------------------------------------------------------------*/

	public static void main(String[] args) throws FileNotFoundException{

		
		String filename=args[0];
		
		/*--------------YOU NEED TO EDIT THESE VALUES-------------*/
		int colors=10;
		double init_temp=0;
		int disp=300;
		/*--------------------------------------------------------*/
		
		
		/*
		disp controls after how many iterations you want to see your graph
		set it to a negative number if you don't want to see it at all
		(you'll still see your final graph)
		*/
		Annealer gc=new Annealer(colors, disp, filename);
		gc.anneal(init_temp);
		
		for(int i=0; i<gc.N; i++)
			System.out.print(gc.best_state[i]+" ");
		System.out.println();
		System.out.println(gc.best_cost);
		
		gc.display_G(gc.best_state, 5, 1);
	}



}

