# Batch Processing Exercises

### Objective

This exercise will help you get familiar with Hadoop. You will also get experience coding with the Mrjob library that helps you write and run Hadoop Streaming jobs.

### What is Hadoop?

Hadoop is an open-source software framework for storing data and running applications on clusters of commodity hardware. It provides massive storage for any kind of data, enormous
processing power and the ability to handle virtually limitless concurrent tasks or jobs. In short, it is a framework that allows you to first store Big Data in a distributed environment, so that you can process it parallelly. There are basically two components in Hadoop:

![](../../../../../../var/folders/3l/f7kskvz92zn732y9z9cf5pvh0000gn/T/TemporaryItems/NSIRD_screencaptureui_XjipVK/Screen Shot 2022-11-29 at 12.23.29 PM.png)

### Complete the following exercises:

This application should use the MrJob library to count the lines, words and the number of characters. Your task is to complete the code for the mapper and reducer.

For more information about MrJob, please see the following documentation: https://mrjob.readthedocs.io/en/latest/. 

1. Complete the functions _mapper_ and _reducer_ in part1 > _mr_chars_words_lines_count.py_ to produce a count of the characters, words and lines in a collection of text files.
2. Test your code with the command:
```python mr_chars_words_lines_count.py wikipedia > out.txt```.
3. go to [PCRS](https://pcrs.teach.cs.toronto.edu/ECE1779-2022-09/content/quests) to answer the related question.
