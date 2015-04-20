test_text=[['First title', 'This is the first text'],['Second title', 'This is the second text']]


def generate(lesson_name, text):
	print '''
	   <div class="lesson">
      
             <h2>'''+ lesson_name + '</h2>'
        for concepts in text:
            title = concepts[0]
    	    description = concepts[1]
            print '''
               <div class="concept">

                 <h3>''' +title + '</h3>' + '''
                  
                   <p>
            ''' + description + '''
                   </p>
                
               </div>'''
   
        print '''            </div> '''  


generate('Session X', test_text)#program takes two inputs: one is the name of the lesson(which in my case is "Session #"), and the other is a list which contains lists with the concepts of each lesson in the format of [concept heading, concept body]. Using for, I can format lessons with 2 concepts or 200. Getting the indentation is something I'm still working on. But I didnt want to miss the stage 2 deadline again.


 
    
