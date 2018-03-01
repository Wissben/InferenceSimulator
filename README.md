# InferenceSimulator
This project is in collaboration with [ressay](https://github.com/ressay) and it's basically a minor fork of his [repository](ressay), thanks to him who did the important part of converting a propositional logic formula into its CNF form, more specifically into the [DIMACS](http://people.sc.fsu.edu/~jburkardt/data/cnf/cnf.html) format.
 ## Dpenendencies 
* You will need to install [Python](https://python.org), we used **Python2.7** in our tests.
* You will also need to install the `antlr4-python2-runtime` python package via `pip` withe following command     
  `sudo pip install antlr4-python2-runtime`
* The `UBCSAT` SAT solver, you can find it [here](http://ubcsat.dtompkins.com/downloads)
 ## Utilisation 
 To start the inference engine just launch the `main.py` script with its arguments : 
  * The knowledge base in its [DIMACS](http://people.sc.fsu.edu/~jburkardt/data/cnf/cnf.html) format.
  * The new knowledge base also in the DIMACS format
  * The propositional logic formula betweet `" "` using the logical connectors and parentheses : 
    * `->` logical implication.
    * `<->` logical equivalence.
    * `v` logical OR.
    * `^` logical AND.
    * `-` logical NOT.
    * `( )` parentheses.
  ### Example 
  Let's say that in the input.cnf file you have the following data : <br />
  **p cnf 2 2 <br />
  -1 2 0 <br />
  1 0 <br />**
  (Please refer to the [DIMACS format page](http://people.sc.fsu.edu/~jburkardt/data/cnf/cnf.html) to understand this codification)
  One formula **F** that we can deduce from this knowledge base is : <br />
  `2 v 1`
  The command would be : <br />
  `python main.py input.cnf "-(2 v 1)"`<br />
  If the SAT solver can't find any solution to this instance, then we can conclude that **F** is a logical consequence of the knowledge base in input (**KNOWLEDGE BASE => F**).
  ## Credit 
  Made with :heart: by [Ressay](https://github.com/ressay) and [Wiss](https://github.com/Wissben). 
