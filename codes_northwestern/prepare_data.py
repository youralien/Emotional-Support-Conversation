import os
import json
import pandas as pd

esconv_datapath = os.path.join('..', 'ESConv.json')
strategy_datapath = os.path.join('..', 'strategy.json')

def help_provider_responses_filtered_by(filt, esconv_data):
  output_list = []

  for i in range(len(esconv_data)):
    dialog = esconv_data[i]['dialog']
    for j in range(len(dialog)):
      if dialog[j]['speaker'] == 'supporter':
        if dialog[j]['annotation']['strategy']:
          if dialog[j]['annotation']['strategy'] == filt:
            output_list.append(dialog[j]['content'])

  print(len(output_list))
  return output_list

def create_training_data(strategies_to_use, responses_data):
  labels = []
  response_texts = []
  for strategy, responses in responses_data.items():
    if strategy in strategies_to_use:
      n_responses = len(responses)
      labels.extend([strategy]*n_responses)
      response_texts.extend(responses)

  df = pd.DataFrame({"strategy": labels, "text": response_texts})
  return df

# all the strategies

def main():
    with open(esconv_datapath, 'r') as data:
      esconv_data = json.load(data)
    len(esconv_data)

    with open(strategy_datapath, 'r') as data:
      strategies = json.load(data)
    strategies_clean = [strat.strip("[]") for strat in strategies]
    strategies_clean

    # Create data mapping from Conversation Responses and Strategy Labels
    responses_data = {}
    for strategy in strategies_clean:
      responses_data[strategy] = help_provider_responses_filtered_by(strategy, esconv_data)
    dataf = create_training_data(strategies_clean, responses_data)

    return dataf

if __name__ == "__main__":
    dataf = main()
