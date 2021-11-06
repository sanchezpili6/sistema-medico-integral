from django.http.response import FileResponse
from app.urls import router
from history.models import History
from prescription.models import Prescription
import qrcode
import qrcode.image.svg
from io import BytesIO

from utils.mixins import (
    BaseGenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
)

from rest_framework.response import Response
from rest_framework import mixins, status, viewsets
from rest_framework.permissions import AllowAny

from prescription import serializers

from fpdf import FPDF
import base64


class PrescriptionViewSet(ListModelMixin,
                          viewsets.GenericViewSet,
                          BaseGenericViewSet):

    serializer_class = serializers.PrescriptionSerializer

    list_serializer_class = serializers.RetrievePrescriptionSerializer

    retrieve_serializer_class = serializers.RetrievePrescriptionSerializer

    permission_classes = [AllowAny]
    queryset = Prescription.objects.all()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        prescription = serializer.save()

        response_serializer = self.get_serializer(prescription, action='retrieve')
        return Response(
            data=response_serializer.data,
            status=status.HTTP_201_CREATED
        )

class PDFViewSet(mixins.CreateModelMixin,
                 viewsets.GenericViewSet,
                 BaseGenericViewSet):
    permission_classes = [AllowAny]
    def create(self, request, *args, **kwargs):

        pk = request.data['pk']

        try:
            prescription = Prescription.objects.get(pk=pk)
        except:
            return Response(
                data={"Error": "Prescription does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )

        response_treatments = ""
        doctor = prescription.doctor
        patient = prescription.patient
        treatments = History.objects.filter(
            doctor=doctor,
            patient=patient
        )
        for treatement in treatments.iterator():
            response_treatments += (treatement.treatment)+','
        qr = qrcode.QRCode()
        qr.add_data('http://localhost:8080/doctor/certificado/prescription.doctor.certificate')
        qr.make()
        img = qr.make_image()  
        img.save('qr.png') 
        pdf = FPDF()
  
        # Add a page
        pdf.add_page()

        pdf.set_font("Arial", size = 18)
        
        pdf.cell(200, 50, txt = "Receta médica", 
                ln = 1, align = 'C')

        
        pdf.cell(200, 30, txt = "Paciente: " + prescription.patient.name + prescription.patient.last_name,
                ln = 2, align = 'L')

        pdf.cell(200, 30, txt = "Nombre médico: " + prescription.doctor.name,
                ln = 2, align = 'L')

        pdf.cell(200, 30, txt = "Tratamientos: " + response_treatments,
                ln = 2, align = 'L')

        pdf.cell(200, 30, txt = "Medicamento recetado: " + prescription.medicine,
                ln = 2, align = 'L')


        pdf.cell(200, 30, txt = "Cédula profesional escrito: " + prescription.doctor.certificate,
                ln = 2, align = 'L')
        
        pdf.cell(200, 30, txt = "QR: ",
        ln = 2, align = 'L')
        pdf.image('qr.png', x = None, y = None, w = 0, h = 0, type = '', link = '')
        pdf.output("receta.pdf")  


        return FileResponse(open('receta.pdf', 'rb'), content_type='application/pdf')


router.register(
    r'prescription/create',
    PrescriptionViewSet,
    basename="prescription"
)

router.register(
    r'prescription/pdf',
    PDFViewSet,
    basename="prescription"
)
