import pandas as pd  # type: ignore
import matplotlib.pyplot as plt
import asyncio
from models.part_model import get_parts, get_part
from models.feature_data_model import get_features_value
from models.detail_model import *
from services.envelope_service import find_signal_envelopes
from services.average_service import find_average_value
from utils.logger import logger


def plot_signals_with_envelopes(df, part_name, signal_values, min_indices, max_indices):
    """
    Plot signal data dengan high dan low envelopes
    """
    plt.figure(figsize=(15, 7))

    # Plot signal asli
    plt.plot(df["datetime"], signal_values, "b-", alpha=0.5, label="Signal")

    # Plot envelopes
    plt.plot(
        df["datetime"].iloc[max_indices],
        signal_values[max_indices],
        "g-",
        label="High Envelope",
        markersize=10,
    )
    plt.plot(
        df["datetime"].iloc[min_indices],
        signal_values[min_indices],
        "r-",
        label="Low Envelope",
        markersize=10,
    )

    plt.title(f"Signal Data dengan High/Low Envelopes: {part_name}")
    plt.xlabel("Tanggal dan Waktu")
    plt.ylabel("Nilai Signal")
    plt.grid(True, alpha=0.3)

    # Format x-axis
    plt.gcf().autofmt_xdate()

    plt.legend()
    plt.tight_layout()
    # plt.show()
    plt.savefig("./public/result/signal_envelopes.png")


def one_percent_condition_calculate(part):
    data = get_features_value(part_id=part[0])
    df = pd.DataFrame(data, columns=["id", "value", "datetime", "part_id"])
    signal_values = df["value"].values

    # find average value
    average_value = find_average_value(signal_values)
    logger.info(f"Average value for part {part[1]}: {average_value}")

    return average_value


def calculate(part):
    data = get_features_value(part_id=part[0])

    # Convert to DataFrame if not already
    df = pd.DataFrame(data, columns=["id", "value", "datetime", "part_id"])

    # Tampilkan informasi data
    # print("Info Dataset:")
    # print(f"Jumlah total record: {len(df)}")
    # print(f"5 data teratas:\n{df.head()}")
    # print(f"Rentang waktu: {df['datetime'].min()} sampai {df['datetime'].max()}")

    signal_values = df["value"].values
    min_indices, max_indices = find_signal_envelopes(signal_values)

    # plot_signals_with_envelopes(
    #     df,
    #     part_name=part[1],
    #     signal_values=signal_values,
    #     min_indices=min_indices,
    #     max_indices=max_indices,
    # )

    # Calculate average value
    max_average = find_average_value(signal_values[max_indices])
    min_average = find_average_value(signal_values[min_indices])

    one_percent_condition = float(one_percent_condition_calculate(part))

    if max_average <= 0 or min_average <= 0:
        # interpolate this, cause the average can't be < 0
        min_average = 10
        max_average = min_average + 10

    range = (max_average - min_average) + 20

    lower_threshold = float(max_average + 15)
    upper_threshold = float(max_average + range + 10)

    detail = get_detail(part[0])

    if detail:
        update_detail(part[0], upper_threshold, lower_threshold, one_percent_condition)
    else:
        create_detail(part[0], upper_threshold, lower_threshold, one_percent_condition)


def main():
    logger.info("Start calculating signal envelopes and average values")
    parts = get_parts()

    try:
        for part in parts:
            calculate(part)
            logger.info(f"Part {part[1]} done")

        logger.info("All parts done")
    except Exception as e:
        logger.error("An exception occurred: ", e)


if __name__ == "__main__":
    main()
