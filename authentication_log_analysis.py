
import pandas as pd

# Load sample authentication logs
logs = pd.read_csv("authentication_logs.csv")

# Count failed login attempts by source IP
failed_logins = (
logs[logs["status"] == "Failed"]
.groupby("source_ip")
.size()
.reset_index(name="failed_attempts")
)

# Flag IP addresses with five or more failed attempts
failed_logins["alert"] = failed_logins[
"failed_attempts"
].apply(
lambda count: "Suspicious" if count >= 5 else "Normal"
)

# Display and save analysis results
print("Authentication Log Analysis")
display(failed_logins)

failed_logins.to_csv("suspicious_logins.csv", index=False)
print("Analysis completed successfully.")
