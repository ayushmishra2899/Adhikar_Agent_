def generate_whatsapp_message(user, schemes):
    msg = f"Namaste {user['name']} 👋\n\n"
    msg += "Aap in sarkari yojnaon ke liye eligible hain:\n\n"

    for s in schemes:
        msg += f"✅ {s['name']} – {s['benefit']}\n"

    msg += "\nHumne aapke liye form bhi bhar diya hai 🙏"
    return msg