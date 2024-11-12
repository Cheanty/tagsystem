from flask import *
import os
# 创建Flask应用实例
app = Flask(__name__, static_folder='static')

# 相关配置

## 长传文件的保存路径
UPLOAD_FOLDER = '/home/work/tagsystem/upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'csv'}

# 上传首页
@app.route('/',methods=['GET'])
def index():
    ns = request.args.get('name', 'Guest')
    return render_template('index.html',name=ns)

@app.route('/submit',methods=['POST'])
def submit():
    if request.method == 'POST':
        input_text = request.form['text_input']
        return f"你输入的内容是: {input_text}"

# 检查文件扩展名是否符合要求
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# 文件上传处理路由
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return '没有文件被上传'
    
    file = request.files['file']
    
    # 检查用户是否选择了文件
    if file.filename == '':
        return '没有选择文件'
    
    # 检查文件是否符合允许的格式
    if file and allowed_file(file.filename):
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)  # 保存文件到指定目录
        return f'文件 {filename} 上传成功！保存路径为 {file_path}'
    
    return '文件类型不允许上传'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050,debug=True)
