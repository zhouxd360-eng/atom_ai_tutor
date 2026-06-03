import gradio as gr

def chat(message, history):
    return f"收到消息: {message}"

with gr.Blocks(title="atom_ai_tutor") as demo:
    gr.Markdown("# atom_ai_tutor 智能家庭教育辅导助手")
    gr.Markdown("基于本地 LLM + RAG + 多模态 OCR/ASR 的私有家庭教育辅助系统")
    
    with gr.Tab("学习对话"):
        chatbot = gr.ChatInterface(chat)
    
    with gr.Tab("学生管理"):
        gr.Markdown("学生信息管理")
    
    with gr.Tab("学习统计"):
        gr.Markdown("学习数据统计")
    
    with gr.Tab("文件上传"):
        gr.Markdown("上传学习资料")
        gr.File(file_types=["image", "audio", "video", "pdf"])

if __name__ == "__main__":
    demo.launch()