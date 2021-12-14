<a href="url"><img src="/assets/logo.png" align="left" height="60" width="60" ></a>
# Chatbot Created for D-590 FA2021
Chatbot for D-590 FA2021


![screenshot](/assets/screenshot_local.png)


## Description

QA chatbot is trained with [roberta-base-squad2 model](https://huggingface.co/deepset/roberta-base-squad2) fine-tuned on [WikiQA dataset](https://huggingface.co/datasets/wiki_qa). Code to prepare the data and train the model can be found in [training_model_on_WikiQA.ipynb](https://github.com/mparoca/chatbot_D-590/blob/main/training_model_on_WikiQA.ipynb) and is partly based on these two notebooks: 

- https://towardsdatascience.com/how-to-fine-tune-a-q-a-transformer-86f91ec92997 
- https://colab.research.google.com/github/fastforwardlabs/ff14_blog/blob/master/_notebooks/2020-05-19-Getting_Started_with_QA.ipynb?pli=1&authuser=1#scrollTo=bgYVkF2RmHPK

When the user enters a query, the [wikipedia library](https://pypi.org/project/wikipedia/) is used to extract the initial paragraphs of an entry that matches the user query. The fine-tuned RoBERTa model is then used to select the location of the response that best matches the query given the context. 

## Deployment

App is currently deployed [here](http://chatbot-d590.herokuapp.com/)

### Plotly Dash

The app was built on [Dash](https://plot.ly/dash), which is a simple and effective way to bind a user interface around Python code. 

### GitHub Integration (Heroku GitHub Deploys)
The app is currently deployed using Heorku through GitHub integration on the Heroku website. [GitHub integration](https://devcenter.heroku.com/articles/github-integration) is configured for a Heroku app and manually deployed, which creates an immediate deployment of the master branch from the current [GitHub repo](https://github.com/mparoca/chatbot_D-590). 

---------------------------------------

Deployed app is using pre-trained minimal model [bert-medium-squad2-distilled](https://huggingface.co/deepset/bert-medium-squad2-distilled). To use the model fine-tuned in [training_model_on_WikiQA.ipynb](https://github.com/mparoca/chatbot_D-590/blob/main/training_model_on_WikiQA.ipynb) or your own fine-tuned model change [get_answer.py](https://github.com/mparoca/chatbot_D-590/blob/main/get_answer.py)

Chatbot front-end partly based on: https://github.com/plotly/dash-sample-apps/tree/main/apps/dash-chatbot

Theme: https://bootswatch.com/vapor/ 
Icons: https://fontawesome.com/v5.15/icons?d=gallery&p=2
