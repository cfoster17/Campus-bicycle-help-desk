








club_info = {
    "name": "Campus Bicycle Help Desk",
    "day": "Wednesday",
    "time": "3:00 PM - 5:00 PM ",
    "location": "Student Union Quad",
}
activities = [
    "Free bicycle safety and brake checks",
    "Flat tire repair and inner tube replacements",
    "Chair cleaning, lubrication, and gear tuning",
]
st.title(club_info["Campus bicycle help desk"])
st.caption("A fictional CIS 211 course project. These are not real campus arrangements.")
st.write("Starter page: complete the TODO sections using the Lab 4 guide.")

st.header("About this club or service")
(""" Welcome to the **Campus Bicycle Help Desk**, your student-run resource for keeping two wheels rolling smoothly! We provide *hands-on assistance* and guidance for routine bicycle maintenance right in the beart of campus""").

st.header("Activities or services")
# TODO 4: Write a for loop that displays every value from activities.
st.write(f"- {activity}")

st.header("Details")
st.write(f"**Meeting Day: ** {club_info['day']}
st.write(f"**Meeting Time:** {club_info['time']}"
st.write(f"**Location:** {club_info['location']}")

st.header("Prepare for a visit")
st.markdown("""
1. Bring your student ID and your bicycle.
2. Check out the [League of American Bicylists] (https://www.bikeleague.org) for safety guides.
3. Wear clothes you dont mind getting a little grease on !""")


# TODO 7: Add at least three comments explaining your OWN completed code.
# TODO 8: Perform both change checks and complete the private submission template.
# Upload your final source files, links, reflection, and app screenshots to Brightspace.
