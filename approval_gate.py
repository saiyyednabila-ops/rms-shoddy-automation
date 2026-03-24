import time

class ApprovalGate:
    def __init__(self):
        self.approval = False

    def display_summary(self, entries):
        print("Summary of Prepared Entries:")
        for entry in entries:
            print(f"- {entry}")

    def request_approval(self):
        response = input("Do you approve the updates? (yes/no): ").strip().lower()
        if response == 'yes':
            self.approval = True
        else:
            print("Update not approved. Exiting...")
            exit()

    def proceed_with_updates(self, entries):
        if not self.approval:
            print("Waiting for approval...")
            self.request_approval()
        print("Proceeding with RMS updates...")
        # Place logic for RMS updates here
        time.sleep(1)  # Simulating updates
        print("RMS updates completed successfully.")

# Example usage:
if __name__ == '__main__':
    entries = ["Entry 1", "Entry 2", "Entry 3"]  # Replace with actual data
    gate = ApprovalGate()
    gate.display_summary(entries)
    gate.proceed_with_updates(entries)