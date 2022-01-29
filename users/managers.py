# from django.contrib.auth.base_user import BaseUserManager


# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         if email is None:
#             raise TypeError("User must enter his email.")

#         user = self.model(
#             email=self.normalize_email(email),
#             is_active=True,
#             is_superadmin=False,
#         )
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, password=None):
#         if email is None:
#             raise TypeError("User must enter his email.")

#         user = self.model(
#             email=self.normalize_email(email),
#             is_active=True,
#             # is_superadmin=True,
#             is_superuser=True,
#             is_staff=True,
#             user_type="admin",
#         )
#         user.set_password(password)
#         user.save()
#         return user
