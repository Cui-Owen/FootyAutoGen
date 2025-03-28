# FootyAutoGen
An automatic football news summarizer and publisher using AI

football-ai-media/
│
├── config/                   # 配置文件目录
│   ├── config.yaml           # 系统全局配置（API Key、抓取源、时间间隔等）
│   └── prompts/              # 存放Prompt文件
│       └── summary_prompt.txt
│
├── src/                      # 源码根目录
│   ├── crawler/              # 新闻抓取模块
│   │   ├── espn.py           # ESPN网站抓取脚本
│   │   ├── football_italia.py# Football Italia抓取脚本
│   │   └── utils.py          # 通用抓取函数
│   │
│   ├── processor/            # 语言模型处理模块
│   │   ├── deepseek_api.py   # 调用DeepSeek模型的封装
│   │   └── translator.py     # 翻译与摘要模块
│   │
│   ├── images/               # 图像匹配模块（第二阶段再创建）
│   │   ├── downloader.py
│   │   └── matcher.py
│   │
│   ├── publisher/            # 发布模块（后期创建）
│   │   ├── weibo_publisher.py
│   │   └── utils.py
│   │
│   ├── storage/              # 数据存储模块（第二阶段创建）
│   │   ├── database.py
│   │   └── models.py
│   │
│   ├── scheduler/            # 调度模块（后期创建）
│   │   └── scheduler.py
│   │
│   ├── logs/                 # 日志文件夹（存放运行日志）
│   └── main.py               # 程序入口文件
│
├── scripts/                  # 一些辅助脚本（比如数据库初始化）
│   └── init_db.py
│
├── data/                     # 临时数据目录（抓取的原始网页、生成文本）
│
├── media/                    # 下载的图片临时存储目录
│
├── tests/                    # 单元测试文件夹（可选）
│   ├── test_crawler.py
│   └── test_processor.py
│
├── .gitignore                # git忽略文件（例如API密钥、临时数据、图片）
├── Dockerfile                # 后期用于部署
├── requirements.txt          # Python依赖文件
└── README.md                 # 项目说明文档
