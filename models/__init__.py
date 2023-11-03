#!/usr/bin/python3
from models.engine.file_storage import FileStorage

storage = FileStorage()
"""Crete an unique FileStorage instance for our application"""
storage.reload()
"""Call reload mwthod on this variable"""
