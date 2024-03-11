import tiktoken 

cl100k_base = tiktoken.get_encoding("cl100k_base") 

enc = tiktoken.Encoding( 
    name="gpt-35-turbo",  
    pat_str=cl100k_base._pat_str, 
    mergeable_ranks=cl100k_base._mergeable_ranks, 
    special_tokens={ 
        **cl100k_base._special_tokens, 
        "<|im_start|>": 100264, 
        "<|im_end|>": 100265
    } 
) 

tokens = enc.encode( 
    "<|im_start|>user\nHello<|im_end|><|im_start|>assistant",  
    allowed_special={"<|im_start|>", "<|im_end|>"} 
) 

assert len(tokens) == 7 
assert tokens == [100264, 882, 198, 9906, 100265, 100264, 78191]