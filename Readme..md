# Auto_replace小工具使用手册

## 1.文件结构

- **auto_replace**
  - auto_replace.exe 
  - Corpus.txt
  - replace_text.txt
  - replaced_text.txt
  - replace_result.txt

## 2.使用环境

- **Windows环境**

## 3.使用步骤

- 在`Corpus.txt`文件里放入原始文本
- 在`replace_text.txt`里放入替换词，每个单词占一行，如果是短语，用空格连接组成该短语的单词即可，仍然是一个短语占一行，也就是一个token（即最小单位，广义上的单词，可以是短语）占一行
- 在`replaced_text.txt`里放入原始文本中需要被替换掉的单词/短语，规则仍然是一行一个token
- 执行`auto_replace.exe `文件，就会在文件夹里自动生成`replace_result.txt`文件，即为替换完后的文本

## 4.最近更新

- 2021.5.3
  - 更新了执行exe文件后的提示内容，便于根据提示进行操作

## 5.反馈与联系

- 使用中出现的问题可以联系donghaotian@tju.edu.cn