# import pandas as pd
# import matplotlib.pyplot as plt

# # ===============================
# # Load Dataset
# # ===============================
# df = pd.read_csv(r"C:\Users\ASUS TUF\Downloads\funnel_events_sample.csv")

# # ===============================
# # Display Basic Information
# # ===============================
# print("First 5 Rows:")
# print(df.head())

# print("\nColumns:")
# print(df.columns)

# # ===============================
# # Remove Duplicate Rows
# # ===============================
# print("\nDuplicate Rows Before:", df.duplicated().sum())
# df.drop_duplicates(inplace=True)
# print("Duplicate Rows After:", df.duplicated().sum())

# # ===============================
# # Convert Timestamp
# # ===============================
# df["timestamp"] = pd.to_datetime(df["timestamp"])

# # ===============================
# # Define Funnel Order
# # (Edit only if your step names differ)
# # ===============================
# funnel_order = [
#     "Visited Site",
#     "Signup Started",
#     "Details Filled",
#     "Email Verified",
#     "Purchase Completed"
# ]

# # Convert step column to ordered category
# df["step"] = pd.Categorical(
#     df["step"],
#     categories=funnel_order,
#     ordered=True
# )

# # ===============================
# # Count Unique Users at Each Stage
# # ===============================
# stage_users = (
#     df.groupby("step")["user_id"]
#     .nunique()
#     .reindex(funnel_order)
# )

# # ===============================
# # Create Funnel Report
# # ===============================
# report = pd.DataFrame({
#     "Stage": stage_users.index,
#     "Unique Users": stage_users.values
# })

# # ===============================
# # Conversion Rate
# # ===============================
# conversion = [100]

# for i in range(1, len(report)):
#     prev = report.loc[i-1, "Unique Users"]
#     curr = report.loc[i, "Unique Users"]

#     if prev == 0:
#         conversion.append(0)
#     else:
#         conversion.append(round((curr / prev) * 100, 2))

# report["Conversion Rate (%)"] = conversion

# # ===============================
# # Drop-off
# # ===============================
# dropoff = [0]

# for i in range(1, len(report)):
#     prev = report.loc[i-1, "Unique Users"]
#     curr = report.loc[i, "Unique Users"]
#     dropoff.append(prev - curr)

# report["Drop-off Users"] = dropoff

# # ===============================
# # Biggest Drop-off
# # ===============================
# # ===============================
# # Biggest Drop-off
# # ===============================

# # Ignore the first row because it has no previous stage
# dropoff_data = report.iloc[1:]

# largest_drop = dropoff_data["Drop-off Users"].idxmax()

# print("\n========== Biggest Drop-off ==========")
# print(f"From : {report.loc[largest_drop-1, 'Stage']}")
# print(f"To   : {report.loc[largest_drop, 'Stage']}")
# print(f"Users Lost : {report.loc[largest_drop, 'Drop-off Users']}")

# print(df.columns.tolist())
# print(df["step"].unique())

# # ===============================
# # Visualization
# # ===============================
# plt.figure(figsize=(9,5))
# plt.bar(report["Stage"], report["Unique Users"])
# plt.title("User Funnel Analysis")
# plt.xlabel("Stages")
# plt.ylabel("Unique Users")
# plt.xticks(rotation=20)
# plt.tight_layout()
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# Load Dataset
# ==========================================
df = pd.read_csv(r"C:\Users\ASUS TUF\Downloads\funnel_events_sample.csv")

# ==========================================
# Basic Information
# ==========================================
print("First 5 Rows:\n")
print(df.head())

print("\nColumns:")
print(df.columns.tolist())

# ==========================================
# Remove Duplicates
# ==========================================
print("\nDuplicate Rows Before:", df.duplicated().sum())

df.drop_duplicates(inplace=True)

print("Duplicate Rows After :", df.duplicated().sum())

# ==========================================
# Convert Timestamp
# ==========================================
df["timestamp"] = pd.to_datetime(df["timestamp"])

# ==========================================
# Funnel Order
# ==========================================
funnel_order = [
    "visited_site",
    "signup_started",
    "details_filled",
    "email_verified",
    "purchase_completed"
]

# ==========================================
# Count Unique Users at Each Stage
# ==========================================
stage_users = (
    df.groupby("step")["user_id"]
      .nunique()
      .reindex(funnel_order, fill_value=0)
)

# ==========================================
# Create Report
# ==========================================
report = pd.DataFrame({
    "Stage": stage_users.index,
    "Unique Users": stage_users.values
})

# ==========================================
# Conversion Rate
# ==========================================
conversion = []

for i in range(len(report)):
    if i == 0:
        conversion.append(100.00)
    else:
        prev = report.loc[i-1, "Unique Users"]
        curr = report.loc[i, "Unique Users"]

        if prev == 0:
            conversion.append(0)
        else:
            conversion.append(round((curr / prev) * 100, 2))

report["Conversion Rate (%)"] = conversion

# ==========================================
# Drop-off Users
# ==========================================
dropoff = [0]

for i in range(1, len(report)):
    prev = report.loc[i-1, "Unique Users"]
    curr = report.loc[i, "Unique Users"]

    dropoff.append(prev - curr)

report["Drop-off Users"] = dropoff

# ==========================================
# Display Report
# ==========================================
print("\n========== USER FUNNEL REPORT ==========\n")
print(report)

# ==========================================
# Biggest Drop-off
# ==========================================
largest_drop = report["Drop-off Users"][1:].idxmax()

print("\n========== BIGGEST DROP-OFF ==========")
print("From Stage :", report.loc[largest_drop-1, "Stage"])
print("To Stage   :", report.loc[largest_drop, "Stage"])
print("Users Lost :", report.loc[largest_drop, "Drop-off Users"])

# ==========================================
# Visualization
# ==========================================
plt.figure(figsize=(9,5))
plt.bar(report["Stage"], report["Unique Users"])

plt.title("User Funnel Analysis")
plt.xlabel("Funnel Stage")
plt.ylabel("Unique Users")

plt.xticks(rotation=20)

for i, value in enumerate(report["Unique Users"]):
    plt.text(i, value + 1, str(value), ha="center")

plt.tight_layout()
plt.savefig("user_funnel_analysis.png", dpi=300, bbox_inches="tight")
plt.show()