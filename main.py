# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 12:01:34 2024

@author: arpit
"""

import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import json
from fastapi.middleware.cors import CORSMiddleware