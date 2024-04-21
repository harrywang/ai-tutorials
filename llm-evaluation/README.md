# (Anon) CNN/DailyMail Processing 
This dataset is used and described in [Nallapati (2016)](https://arxiv.org/pdf/1602.06023.pdf) for abstractive text summarization. It is called "anonymized" since it uses tags instead of named entity. 


# Getting started

## Prerequisites
* Get StanfordCoreNLP tool: `./get_corenlp.sh`
* Install Python requirements: `pip install -r requirements.txt`
* Get the data from the [official link](https://cs.nyu.edu/~kcho/DMQA/).
    * you need to get both "Questions" and "Stories" for both CNN and DailyMail: total: 4 archives (`cnn.tgz`, `dailymail.tgz`, `cnn_stories.tgz`, `dailymail_stories.tgz`)
    * put everything in a sub-folder `./data`
    * extract it `tar -xvzf cnn.tgz` etc...
    * You must have the following file tree:
      ```
        ./data
            ./cnn
                ./questions
                ./stories
            ./dailymail
                ./questions
                ./stories
      ```

## Process the data
* set the classpath: `source load_corenlp.sh` (it supposes that you have corenlp in the current folder)
* run the processing script: `./process.py -d ./data -o ./processed -c ./stanford-corenlp`
    * **NOTE:** It may take quite a long time (~60mins)

You will get all the output in the `processed` directory, in particular, 3 sub-directory `training/`, `validation/`, `test/`, and in each:
* `stories`: file with one "story" per line (i.e. the source text)
* `highlights`: file with one "highlight" per line (i.e. summary, the reference)
* `entities`: file with one path per line, that corresponds to the entity file associated with the training pair.  
* a lot of `.entities` file that contains entities mapping for each training pair.


## Replace tags by original text
After training/inference, you will get text files with `@entity` tags. You can use `unanonymize.py` in order to replace those tags with the corresponding entities.

```
./unanonymize.py [-h] -f FILE -fl ENTITIES_FILE_LIST -d ENTITIES_DIR -o OUTPUT
```
* `FILE`:  your prediction file with tags, with 1 sequence per line.
* `ENTITIES_FILE_LIST`: the file with entities files path (produced in the `process` step)
* `ENTITIES_DIR`: the directory containing `.entities` files.
* `OUTPUT`: filepath for output (i.e. full text)


./unanonymize.py -f FILE -fl ENTITIES_FILE_LIST -d ENTITIES_DIR -o OUTPUT

## Calculate ROUGE score
*(I use [`files2rouge`](https://github.com/pltrdy/files2rouge) to calculate ROUGE scores)*


Since the dataset is anonymised one can calculate scores between anon files (with tags) or with full text (must be higher).

Considering you have:
* `predictions` (anonymised prediction)
* `predictions.unan` (unanonymised)
* `test/highlights` (test anon reference)
* `test/highlights.unan` 

You can get: 
* Anon scores:
```
files2rouge ./predictions test/highlights -s scores
```

* Full text scores:
```
files2rouge ./predictions.unan test/highlights.unan -s scores.unan
```



```
brew install openjdk
sudo ln -sfn /opt/homebrew/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk
```
