import os
from dotenv import load_dotenv
from connpass import ConpassEventRequest
from ical import ICalendarWriter
from github import GitHubUploader

load_dotenv()


def main(ics_file="event.ics", prefecture="山梨県"):
    events = ConpassEventRequest(prefecture=prefecture, months=3).get_events()
    events.sort(key=lambda x: x["started_at"])

    calendar_name = f"IT勉強会 - {prefecture}"
    calendar_description = f"{prefecture}で開催されるIT勉強会イベントカレンダー"
    ICalendarWriter(
        events,
        name=calendar_name,
        description=calendar_description
    ).write(ics_file)

    GitHubUploader(
        token=os.getenv("GITHUB_TOKEN"),
        owner=os.getenv("GITHUB_OWNER"),
        repo=os.getenv("GITHUB_REPO")
    ).upload(ics_file)


if __name__ == "__main__":
    main(ics_file="event_minato.ics", prefecture="東京都港区")
    main(ics_file="event_shibuya.ics", prefecture="東京都渋谷区")
    main(ics_file="event_shizuoka.ics", prefecture="静岡県")
    main(ics_file="event_nagano.ics", prefecture="長野県")
