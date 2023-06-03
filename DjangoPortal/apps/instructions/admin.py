from django.contrib import admin

# Register your models here.

from .models import Instruction


@admin.register(Instruction)
class InstructionAdmin(admin.ModelAdmin):
    search_fields = Instruction.SearchableFields
