# Neural_Network_explaination
This is a simple network to Understand, You Can extand this Network and add more Layers in the network but the Idea behind the scene is always same.  

# What is Neural Network :
        A neural network is a series of algorithms that endeavors to recognize underlying relationships in a
        set of data through a process that mimics the way the human brain operates. 
        Neural networks can adapt to changing input; so the network generates the best possible result 
        without needing to redesign the output criteria.
        
   ![](images/index.png)
  
# Feedforword :
  
![](images/neural_network.png)

Output of First Layer is the sumation of multiplied all the input and Weight.
<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;O_i&space;=&space;Input" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;O_i&space;=&space;Input" title="O_i = Input" /></a>   
<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;O_j&space;=&space;Output_1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;O_j&space;=&space;Output_1" title="O_j = Output_1" /></a>  
<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;O_k&space;=&space;Output_2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;O_k&space;=&space;Output_2" title="O_k = Output_2" /></a>  
<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;W_j&space;=&space;Weight_1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;W_j&space;=&space;Weight_1" title="W_j = Weight_1" /></a>  
<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;W_k&space;=&space;Weight_2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;W_k&space;=&space;Weight_2" title="W_k = Weight_2" /></a>   
<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;\sigma&space;=&space;SigmaFunction" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;\sigma&space;=&space;SigmaFunction" title="\sigma = SigmaFunction" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;Output_1&space;=&space;\sigma&space;\left&space;(&space;\sum&space;\left&space;(&space;Input&space;\times&space;Weight_1&space;\right&space;)&space;&plus;&space;Bias_1&space;\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;Output_1&space;=&space;\sigma&space;\left&space;(&space;\sum&space;\left&space;(&space;Input&space;\times&space;Weight_1&space;\right&space;)&space;&plus;&space;Bias_1&space;\right&space;)" title="Output_1 = \sigma \left ( \sum \left ( Input \times Weight_1 \right ) + Bias_1 \right )" /></a>
<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;Output_2&space;=&space;\sigma&space;\left&space;(&space;\sum&space;\left&space;(&space;Output_1\times&space;Weight_2&space;\right&space;)&space;&plus;&space;Bias_2&space;\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;Output_2&space;=&space;\sigma&space;\left&space;(&space;\sum&space;\left&space;(&space;Output_1\times&space;Weight_2&space;\right&space;)&space;&plus;&space;Bias_2&space;\right&space;)" title="Output_2 = \sigma \left ( \sum \left ( Output_1\times Weight_2 \right ) + Bias_2 \right )" /></a>

# Error Calculation: 
        Calculating the Error at the Output_2
  
<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;Error_2&space;=&space;(Output_2&space;\times&space;(1-Output_2))&space;\times&space;(Target&space;-&space;Output_2)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;Error_2&space;=&space;(Output_2&space;\times&space;(1-Output_2))&space;\times&space;(Target&space;-&space;Output_2)" title="Error_2 = (Output_2 \times (1-Output_2)) \times (Target - Output_2)" /></a>

        Also write as :
<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;Error_2&space;=&space;\frac{\partial&space;\sigma&space;(Output_2)}{\partial&space;x}\left&space;(&space;Target&space;-&space;Output_2&space;\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;Error_2&space;=&space;\frac{\partial&space;\sigma&space;(Output_2)}{\partial&space;x}\left&space;(&space;Target&space;-&space;Output_2&space;\right&space;)" title="Error_2 = \frac{\partial \sigma (Output_2)}{\partial x}\left ( Target - Output_2 \right )" /></a>
 
        Calculating the error at Output_1 
 
<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;Error_1&space;=&space;(Output_2&space;\times&space;(1-Output_2))&space;\times&space;\sum&space;\left&space;(Error_2&space;\times&space;Weight_2\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;Error_1&space;=&space;(Output_2&space;\times&space;(1-Output_2))&space;\times&space;\sum&space;\left&space;(Error_2&space;\times&space;Weight_2\right&space;)" title="Error_1 = (Output_2 \times (1-Output_2)) \times \sum \left (Error_2 \times Weight_2\right )" /></a>

        Also Write as:
        
<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;Error_1&space;=&space;\frac{\partial&space;\sigma&space;\left&space;(&space;Output_2&space;\right&space;)}{\partial&space;x}&space;\times&space;\sum&space;(Error_2&space;\times&space;Weight_2)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;Error_1&space;=&space;\frac{\partial&space;\sigma&space;\left&space;(&space;Output_2&space;\right&space;)}{\partial&space;x}&space;\times&space;\sum&space;(Error_2&space;\times&space;Weight_2)" title="Error_1 = \frac{\partial \sigma \left ( Output_2 \right )}{\partial x} \times \sum (Error_2 \times Weight_2)" /></a>

# Back Propagation
        Update the Weights
   
<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;Weight_1&space;=&space;Weight_1&space;&plus;&space;Learning&space;Rate&space;\times&space;Error_1&space;\times&space;Input" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;Weight_1&space;=&space;Weight_1&space;&plus;&space;Learning&space;Rate&space;\times&space;Error_1&space;\times&space;Input" title="Weight_1 = Weight_1 + Learning Rate \times Error_1 \times Input" /></a>
  

<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;Weight_2&space;=&space;Weight_2&space;&plus;&space;Learning&space;Rate&space;\times&space;Error_2&space;\times&space;Output_1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;Weight_2&space;=&space;Weight_2&space;&plus;&space;Learning&space;Rate&space;\times&space;Error_2&space;\times&space;Output_1" title="Weight_2 = Weight_2 + Learning Rate \times Error_2 \times Output_1" /></a>

        Update the Bias

<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;Bias_1&space;=&space;Bias_1&space;&plus;&space;LearningRate&space;\times&space;Error_1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;Bias_1&space;=&space;Bias_1&space;&plus;&space;LearningRate&space;\times&space;Error_1" title="Bias_1 = Bias_1 + LearningRate \times Error_1" /></a>


<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;Bias_2&space;=&space;Bias_2&space;&plus;&space;LearningRate&space;\times&space;Error_2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;Bias_2&space;=&space;Bias_2&space;&plus;&space;LearningRate&space;\times&space;Error_2" title="Bias_2 = Bias_2 + LearningRate \times Error_2" /></a>

        Hope you understand the Basic idea behind the Neural Network
        
# Thank You :-
