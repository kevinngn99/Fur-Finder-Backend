from django.contrib import admin
from .models import Pet, PetImage, FidoFinder, HelpingLostPets, LostMyDoggie, PawBoost, PetKey, TabbyTracker

class PetImageInline(admin.TabularInline):
    model = PetImage
    extra = 3

class PetAdmin(admin.ModelAdmin):
    inlines = [PetImageInline, ]

admin.site.register(Pet, PetAdmin)
admin.site.register(FidoFinder)
admin.site.register(HelpingLostPets)
admin.site.register(LostMyDoggie)
admin.site.register(PawBoost)
admin.site.register(PetKey)
admin.site.register(TabbyTracker)
#admin.site.register(ReportedPets)
