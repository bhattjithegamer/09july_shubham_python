import instaloader
name = input("enter insta id")

insta = instaloader.Instaloader()
insta.download_profile(name,profile_name=False)

print("download successfully ! ")