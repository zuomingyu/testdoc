#!/usr/bin/env python
# coding: utf-8
import os
import web

def analysis_module_file(post_str):
    init_dict = {}
    file_path = ''
    for f_type in web.config['lang_list']:
        file_path = os.path.join(web.config['work_dir'], 'langfiles', '%s%s' % (post_str,f_type))
        if os.path.exists(file_path):            
            t_dict = analysis_lang_data(file_path)
            lat_dict = create_format_data(t_dict, post_str)
            if lat_dict:
                return lat_dict
            break
    return init_dict
    
def analysis_lang_data(file_path):
    lang_content = open(file_path).readlines()
    t_dict = {}
    key_word = ''
    for line in lang_content:
        line = line.strip()
        if line[:2] == '#:': ##关键字行
            key_word = line[2:].split('#', 1)[0].strip()
            t_dict[key_word] = []
        elif line=='' or line[0]=='#':
            continue
        else:
            t_dict[key_word].append(line) 
    return t_dict
            
def create_format_data(content_dict, file_name):
    t_dict = {}    
    t_dict['page_title'] = replace_single(content_dict, 'page_title')    
    t_dict['previous_link'] = replace_single(content_dict, 'previous_link')
    t_dict['previous_title'] = replace_single(content_dict, 'previous_title')    
    t_dict['next_link'] = replace_single(content_dict, 'next_link')
    t_dict['next_title'] = replace_single(content_dict, 'next_title')
    side_key_dict = format_content(content_dict, 'side')
    if side_key_dict:
        t_dict['side'] = replace_keyword(side_key_dict, file_name, 'side')
    else:
        t_dict['side'] = ''
    body_dict = format_content(content_dict, 'body')
    if body_dict:
        t_dict['body'] = replace_keyword(body_dict, file_name, 'body')
    else:
        t_dict['body'] = ''
    return t_dict
        
def replace_single(content_dict, key_word): 
    key_word = content_dict.get(key_word, [])   
    if key_word:
        return key_word[0].strip('"')
    else:
        return ''      
    
def format_content(content_dict, key_word):
    content = content_dict.get(key_word, [])
    t_dict = {}
    key = ""
    vals = []
    if not content:
        return t_dict
    for l in content:       
        if l[0] == ':':
            if vals and key:
                t_dict[key] = " ".join(vals)
                vals = []
            key = l.strip()[1:]
        else:
            vals.append(l)                
    if key:
        t_dict[key] = " ".join(vals)    
    return t_dict       
        
def replace_keyword(key_dict, file_name, flag):
    file_path = os.path.join(web.config['work_dir'], 'sourcefile', '%s_%s.html' % (file_name,flag))
    try:
        all_txt = open(file_path).read()
    except:
        print 'READ Source File Failed!'
        return ''    
    for k, v in key_dict.items():
        all_txt = all_txt.replace("$('%s')" % k, v)
    return all_txt


    
        