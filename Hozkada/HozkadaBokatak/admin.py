from django.contrib import admin
from .models import Bezeroa
from .models import Platerra
from .models import Eskaera
from .models import Platerra_Eskaera
from .models import Alergia
from .models import Deskontua
from .models import Deskontua_Platerra
from .models import Alergia_Platerra

# Register your models here.

admin.site.register(Bezeroa)
admin.site.register(Platerra)
admin.site.register(Eskaera)
admin.site.register(Platerra_Eskaera)
admin.site.register(Alergia)
admin.site.register(Deskontua)
admin.site.register(Deskontua_Platerra)
admin.site.register(Alergia_Platerra)