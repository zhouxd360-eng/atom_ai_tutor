# README\.md

## atom_ai_tutor 智能家庭教育辅导助手

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

[![Python Version](https://img.shields.io/badge/Python-3.10-green.svg)](https://www.python.org/downloads/release/python-3100/)

**轻量化 · 全本地私有化 · 碎片化迭代 AI 家庭导师 Agent**

基于本地 LLM \+ RAG \+ 多模态 OCR/ASR 打造的私有家庭教育辅助系统，**所有数据本地留存、不上云、无隐私泄露风险**，专为个人家庭自用设计，支持碎片化时间渐进式开发迭代。

---

## ✨ 核心亮点

- **百分百私有化**：模型、OCR、ASR、知识库全部本地离线运行，学生学情、错题、教材数据不出本机

- **轻量化部署**：无需服务器、无需云服务，普通家用电脑/NAS 即可运行

- **碎片化迭代**：功能原子化拆分，15分钟即可开发一个小功能，边用边更，无需一次性完工

- **多模态适配**：支持试卷图片OCR、语音作业ASR、教材PDF解析、音视频学习资料处理

- **个性化学情**：专属孩子私有向量知识库，精准定位薄弱点，智能出题、生成学习计划

---

## 📁 项目目录结构

```plaintext
atom_ai_tutor/
├── config/                  # 全局配置文件（路径、模型、参数配置）
│   ├── app_config.yaml      # 项目核心配置
│   └── knowledge_std.json   # 中小学课标知识点树形结构
├── frontend/                # 前端交互层
│   └── gradio_main.py       # 快速可视化交互页面
├── api/                     # FastAPI 模块化业务接口
│   ├── student_info/        # 学生档案、性格标签、基础信息模块
│   ├── study_stat/          # 成绩、错题学情统计模块
│   ├── rag_dispatch/        # RAG 知识库检索调度模块
│   ├── plan_task/           # 学习日程、成长计划模块
│   └── multimodal_upload/   # 图片/音频/视频上传调度模块
├── preprocess/              # 本地多模态预处理脚本
│   ├── ocr_paddle.py        # 试卷、课本图片离线OCR识别
│   ├── asr_funasr.py        # 语音离线转文字
│   └── video_parse.py       # 视频抽帧、字幕提取、摘要生成
├── agent_core/              # LLM + RAG Agent 核心引擎
│   ├── model_loader.py      # 本地GGUF量化模型加载
│   ├── agent_study.py       # 学情诊断智能体
│   ├── agent_exam.py        # 个性化出题智能体
│   └── agent_plan.py        # 学习规划智能体
├── data/                    # 全量私有数据存储（可随时备份）
│   ├── sqlite/              # 结构化数据库（学生信息、成绩、计划）
│   ├── vector_db/           # 分孩子独立向量知识库
│   └── raw_file/            # 原始教材、试卷、音视频资源
├── model/                   # 本地量化大模型存放目录
├── requirements/            # 分层轻量化依赖
│   ├── base.txt             # 基础服务依赖
│   ├── multimodal.txt       # 多模态处理依赖
│   └── llm.txt              # 大模型&Agent依赖
├── .gitignore               # 隐私文件、大文件忽略配置
└── main.py                  # 项目统一启动入口

```

---

## 🚀 快速部署

### 1\. 环境准备（Conda 轻量化环境）

```bash
# 创建专属虚拟环境
conda create -n atom_ai_tutor python=3.10 -y

# 激活环境
conda activate atom_ai_tutor

```

### 2\. 安装分层依赖

```bash
pip install -r requirements/base.txt
pip install -r requirements/multimodal.txt
pip install -r requirements/llm.txt

```

### 3\. 项目启动

```bash
python main.py

```

- 后端接口文档：[http://127\.0\.0\.1:8000/docs](http://127.0.0.1:8000/docs)

- 前端交互页面：启动后自动挂载本地端口

---

## 🎯 功能迭代规划（碎片敏捷迭代）

### V0\.1 【当前迭代】基础可用版

- 项目环境\&目录初始化

- 学生档案信息录入、编辑、查询

- 基础数据库结构化存储

### V0\.2 知识库增强版

- PDF教材导入、知识点切片入库

- 基础RAG检索功能落地

- 手动错题录入与归档

### V0\.3 智能学情版

- 试卷图片OCR自动识别错题

- 学情Agent自动分析薄弱知识点

- 针对性个性化出题能力

### V0\.4 多模态全功能版

- 离线语音ASR作业抽查

- 视频学习资料解析归档

- 智能周/月学习计划自动生成

---

## 🔒 隐私安全机制（核心优势）

- **全离线运行**：无任何第三方云端接口调用，所有解析、推理均在本地完成

- **数据完全私有**：学生学情、错题、教材数据仅存储本地/NAS，无自动云同步

- **极简备份**：复制data目录即可完成全量数据备份迁移

- **本地版本管控**：Git本地仓库管理，代码不上传公开平台

---

## 📄 开源协议

本项目基于 **MIT License** 开源，允许自由修改、学习、个人商用、二次分发，仅需保留原始版权声明。

详见：[LICENSE](https://www.doubao.cn)



> （注：文档部分内容可能由 AI 生成）
