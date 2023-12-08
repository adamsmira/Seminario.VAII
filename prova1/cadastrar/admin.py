from django.contrib import admin

from .models import Aluno

admin.site.register(Aluno)

from .models import professor

admin.site.register(professor)

from .models import turma

admin.site.register(turma)

from .models import curso

admin.site.register(curso)

from .models import disciplina

admin.site.register(disciplina)

from .models import DetalheTurma

admin.site.register(DetalheTurma)

from .models import DetalheCurso

admin.site.register(DetalheCurso)

from .models import DetalheDisciplina

admin.site.register(DetalheDisciplina)
