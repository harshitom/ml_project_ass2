models = ['Logistic Regression', 'K-NN', 'SVM', 'DT', 'ANN']
accuracy = [lr_accuracy, knn_accuracy, svm_accuracy, dt_accuracy, ann_accuracy]
precision = [lr_precision, knn_precision, svm_precision, dt_precision, ann_precision]

# Plotting
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

ax[0].bar(models, accuracy, color='blue')
ax[0].set_title('Accuracy of Models')
ax[0].set_ylabel('Accuracy')

ax[1].bar(models, precision, color='green')
ax[1].set_title('Precision of Models')
ax[1].set_ylabel('Precision')

plt.tight_layout()
plt.savefig('model_performance_metrics.png')  # Save snapshot as image
