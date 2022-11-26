from flask import Flask,render_template
import pandas as pd

app=Flask(__name__)

df=pd.read_csv('Project.csv')

df.to_csv('Project.csv',index=None)

@app.route('/')
def csvtohtml():
    data=pd.read_csv('Project.csv')
    return render_template('Filter.html',tables=[df.to_html()],titles=[''])
    
if __name__=='__main__':
                  app.run(host='localhost',port='5000')