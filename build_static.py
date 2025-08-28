from app import app
from flask_frozen import Freezer
import os

# 配置Freezer
app.config['FREEZER_DESTINATION'] = 'static_site'
app.config['FREEZER_RELATIVE_URLS'] = True  # 使用相对URL
freezer = Freezer(app)

if __name__ == '__main__':
    # 确保输出目录存在
    if not os.path.exists(app.config['FREEZER_DESTINATION']):
        os.makedirs(app.config['FREEZER_DESTINATION'])
    
    # 冻结应用（生成静态文件）
    freezer.freeze()
