CUDA_VISIBLE_DEVICES=0 python infer.py \
    --config_name strat \
    --inputter_name strat \
    --add_nlg_eval \
    --seed 0 \
    --load_checkpoint ./DATA/strat.strat/2022-09-27190751.3e-05.16.0gpu/epoch-2.pt \
    --fp16 false \
    --max_input_length 160 \
    --max_decoder_input_length 40 \
    --max_length 40 \
    --min_length 10 \
    --infer_batch_size 2 \
    --infer_input_file ./_reformat/test.txt \
    --temperature 0.7 \
    --top_k 0 \
    --top_p 0.9 \
    --num_beams 1 \
    --repetition_penalty 1 \
    --no_repeat_ngram_size 0
