import argparse
import pandas as pd

from sacrebleu.metrics import BLEU, CHRF


parser = argparse.ArgumentParser()

parser.add_argument(
    "--predictions",
    required=True
)

parser.add_argument(
    "--comet",
    action="store_true"
)

args = parser.parse_args()


df = pd.read_csv(
    args.predictions
)


refs = (
    df["target"]
    .astype(str)
    .tolist()
)


hyps = (
    df["prediction"]
    .astype(str)
    .tolist()
)


bleu = BLEU(
    tokenize="flores200"
)


spbleu = bleu.corpus_score(
    hyps,
    [refs]
).score


chrf = CHRF(
    word_order=2
)


chrfpp = chrf.corpus_score(
    hyps,
    [refs]
).score


print(
    "spBLEU:",
    spbleu
)

print(
    "ChrF++:",
    chrfpp
)


if args.comet:

    from comet import (
        download_model,
        load_from_checkpoint
    )


    model_path = download_model(
        "Unbabel/wmt22-comet-da"
    )


    model = load_from_checkpoint(
        model_path
    )


    data = [
        {
            "src": str(row.source),
            "mt": str(row.prediction),
            "ref": str(row.target)
        }
        for row in df.itertuples(
            index=False
        )
    ]


    output = model.predict(
        data,
        batch_size=8,
        gpus=1
    )


    print(
        "COMET:",
        output.system_score
    )
