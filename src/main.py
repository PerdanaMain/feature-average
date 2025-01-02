import pandas as pd  # type: ignore
import matplotlib.pyplot as plt
from models.part_model import get_parts, get_part
from models.feature_data_model import get_features_value
from services.envelope_service import find_signal_envelopes
from services.average_service import find_average_value


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


def main():
    part = get_part(part_id="414520b7-e7b0-4fea-aa7a-d7b40f444963")
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


if __name__ == "__main__":
    main()
