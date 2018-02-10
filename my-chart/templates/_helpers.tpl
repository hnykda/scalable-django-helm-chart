{{- define "base_labels" }}
{{ .Values.projectIdentifier }}: {{ .Chart.Name }}
release: {{ .Release.Name }}
chart: {{ .Chart.Name }}-{{ .Chart.Version }}
{{- end }}

{{- define "django_labels" }}
{{- include "base_labels" . }}
{{ .Values.appIdentifier }}: {{ .Values.django.app }}
{{ .Values.tierIdentifier }}: {{ .Values.django.tier }}
{{ .Values.roleIdentifier }}: {{ .Values.django.role }}
{{- end }}

{{- define "django_metadata" }}
metadata:
  name: {{ .Chart.Name }}-worker
  labels:
    {{- include "django_labels" . | indent 4 }}
{{- end }}

{{- define "redis_slave_labels" }}
{{- include "base_labels" . }}
{{ .Values.appIdentifier }}: {{ .Values.redis.app }}
{{ .Values.tierIdentifier }}: {{ .Values.redis.tier }}
{{ .Values.roleIdentifier }}: {{ .Values.redis.roleSlave }}
{{- end }}

{{- define "redis_slave_metadata" }}
metadata:
  name: {{ .Chart.Name }}-redis-slave
  labels:
    {{- include "redis_slave_labels" . | indent 4 }}
{{- end }}


{{- define "redis_master_labels" }}
{{- include "base_labels" . }}
{{ .Values.appIdentifier }}: {{ .Values.redis.app }}
{{ .Values.tierIdentifier }}: {{ .Values.redis.tier }}
{{ .Values.roleIdentifier }}: {{ .Values.redis.roleMaster }}
{{- end }}

{{- define "redis_master_metadata" }}
metadata:
  name: {{ .Chart.Name }}-redis-master
  labels:
    {{- include "redis_master_labels" . | indent 4 }}
{{- end }}
