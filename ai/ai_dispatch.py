import ai.ai_gemini as ai_gemini
import ai.ai_groq as ai_groq
import ai.ai_kimi as ai_kimi


def ai_assistant_dispatch(myapp, model, messages, ai_param:tuple={"Output Length": 1024, "Temperature": 0.7, "Top-P": 0.7, "Top-K": 50, "Repetition Penalty": 1.01, 'kimi_chat_id_playground': True}, wx:str="playground"):    
    #try:
    if model == "gemini-pro":
        content, messages = ai_gemini.ai_assistant(model, messages, ai_param)
        dict_ = {}
    elif model == "kimi":
        if hasattr(myapp, 'kimi_playground'):
            kimi_playground = myapp.kimi_playground
        else:
            kimi_playground = {}        
        if hasattr(myapp, 'kimi_chat_id_dict'):
            kimi_chat_id_dict = myapp.kimi_chat_id_dict  # kimi的chat字典
        else:
            kimi_chat_id_dict = {}
        if hasattr(myapp, 'refs_id'):
            refs_id = myapp.refs_id.get(wx, [])
        else:
            refs_id = []
        content, messages, dict_ = ai_kimi.ai_assistant(model, messages, ai_param, key=myapp.key, filepath=myapp.filepath, ai_list=myapp.ai_list, kimi_playground=kimi_playground, refs_id=refs_id, kimi_chat_id_dict=kimi_chat_id_dict, wx=wx)        
    else:
        content, messages, dict_ = ai_groq.ai_assistant(model, messages, ai_param, key=myapp.key)
    return content, messages, dict_
    #except:
        #pass


def ai_assistant_file_dispatch(filepath, key):
    ref_id, key = ai_kimi.ai_assistant_upload_file(filepath, key)
    return ref_id, key


def ai_assistant_image_dispatch(filepath, key):
    ref_id, key = ai_kimi.ai_assistant_upload_image(filepath, key)
    return ref_id, key