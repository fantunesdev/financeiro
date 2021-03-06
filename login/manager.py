from django.contrib.auth.base_user import BaseUserManager


class UsuarioManager(BaseUserManager):
    def create_user(self, nome, email, username, password, date_joined, foto):
        if not email:
            raise ValueError('O campo e-mail não foi informado.')
        if not username:
            raise ValueError('O campo username não foi informado.')
        usuario = self.model(
            nome=nome,
            email=self.normalize_email(email),
            username=username,
            date_joined=date_joined,
            foto=foto
        )
        usuario.set_password(password)
        usuario.save()
        return usuario
