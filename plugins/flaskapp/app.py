from flask import Flask
import dropbox

app = Flask(__name__)

@app.route('/pdflink', methods=['POST', 'GET'])
def pdflink():
    dbx = dropbox.Dropbox("r4ABh_NvBxAAAAAAAAABpyZioVr_ClDgJu4h-lMYDgfFgPSplsKGhQGFzV6YhY2J")
    result = dbx.files_get_temporary_link("/Get Started with Dropbox.pdf")
    return(f'<a href={result.link}>pdf link</a>')

if __name__ == "__main__":
    app.run(debug=True)


    
